/** @type {import('next').NextConfig} */
const nextConfig = {
  // NOTE: Do NOT add typescript.ignoreBuildErrors — TypeScript errors should
  // fail the build so bugs are caught before deployment.
  images: {
    unoptimized: true,
  },
  async rewrites() {
    return process.env.NODE_ENV === 'development'
      ? [
          {
            source: '/api/:path*',
            destination: 'http://127.0.0.1:8000/api/:path*',
          },
        ]
      : []
  },
}

export default nextConfig
